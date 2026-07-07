// HomePage — assembles all section widgets into the full portfolio page layout
import { Hero } from "../../widgets/hero/Hero";
import { Navbar } from "../../widgets/nav/Navbar";

export const HomePage = () => {
    return (
        <main className="min-h-screen bg-background">
           {/*Navbar - always visible as you scroll down*/}
           <Navbar />
           {/*Hero Section - first section visible when page loads*/}
           <Hero />
           {/*About Section - second section visible when you scroll down*/}
           {/*Projects Section - third section visible when you scroll down*/}
           {/*Contact Section - fourth section visible when you scroll down*/}
           {/*Footer - always visible at the bottom of the page*/}
        </main>
    )
};