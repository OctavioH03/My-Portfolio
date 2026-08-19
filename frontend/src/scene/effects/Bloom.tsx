import { Bloom } from "@react-three/postprocessing";

export function BloomEffect() {
    return (
            <Bloom 
                intensity={1.2}
                luminanceThreshold={0.2}
                radius={0.65}
            />
    )
}