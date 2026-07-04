// App — root component: mounts providers, router, and the home page
import { Providers } from "./providers";
import { HomePage } from "../pages/home/HomePage";

export const App = () => {
    return (
        <Providers>
            <HomePage />
        </Providers>
    )
}
export default App;