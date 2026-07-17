// HomePage — assembles all section widgets into the full portfolio page layout
import { Navbar } from "../../widgets/nav/Navbar";
import { Scene } from "../../scene/Scene";

export const HomePage = () => {
    return (
        <main className="min-h-screen bg-background">
           {/*Navbar - always visible as you scroll through the scene*/}
           <Navbar />
           <Scene />
        </main>
    )
};