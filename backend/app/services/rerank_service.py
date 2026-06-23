import cohere
from app.core.logging import get_logger
from app.core.config import Settings
from app.models.retrieval_models import RetrievalChunk
from app.models.chunk_models import ChunkModel
import yaml

# Cohere API response format for reranking:
# {
#   "results": [
#     {
#       "index": 3,   # index of the chunk in the original list
#       "relevance_score": 0.999071
#     },
#     {
#       "index": 4,
#       "relevance_score": 0.7867867
#     },
#     {
#       "index": 0,
#       "relevance_score": 0.32713068
#     }
#   ],
#   "id": "07734bd2-2473-4f07-94e1-0d9f0e6843cf",
#   "meta": {
#     "api_version": {
#       "version": "2",
#       "is_experimental": false
#     },
#     "billed_units": {
#       "search_units": 1
#     }
# }
class RerankService:
    def __init__(self):
        self._logger = get_logger(__name__)
        self._cohere_client = cohere.ClientV2(Settings().COHERE_API_KEY)
    
    def rerank(self, query: str, chunks: list[ChunkModel]) -> list[RetrievalChunk]:
        """ Rerank a list of retrieved chunks so that the most relevant chunks are at the top of the list

        Args:
            query(str): The query to rerank the chunks for
            chunks(list[ChunkModel]): The chunks to rerank
        Returns:
            list[RetrievalChunk]: The reranked chunks
        """
        try:
            yaml_chunks = [yaml.dump(chunk.model_dump()) for chunk in chunks]
            response = self._cohere_client.rerank(
                model=Settings().RERANKING_MODEL,
                query=query,
                documents=yaml_chunks,
                top_n=Settings().RERANKING_TOP_K,
            )
            # Return the top N chunks based on the reranking results
            top_chunks = []
            for result in response.results:
                top_chunks.append(chunks[result.index].model_copy(update={"similarity": result.relevance_score}))

            if top_chunks[0].similarity < Settings().MIN_SIMILARITY_SCORE:
                return []
            return top_chunks

        except Exception as e:
            self._logger.error(f"Error reranking chunks: {e}")
            raise