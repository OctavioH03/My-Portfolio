// Hero widget — name, title, CTA, and background animation panel --> 40/60 split 
import { HeroContent } from "./HeroContent";
import { HeroVisual } from "./HeroVisual";

export const Hero = () => {
    return (
        // Hero section with a 40/60 column layout for content and visual elements
        <section 
            id="hero" 
            className="min-h-screen pt-10"
        >
            <div className="grid min-h-[calc(100vh-2.5rem)] grid-cols-1 lg:grid-cols-[2fr_3fr]">
                {/* Left Panel(40%): Content */}
                <div className="flex items-center justify-center bg-background px-8 py-12 lg:px-12 xl:px-20">
                    <HeroContent title="Octavio Hernandez" description="I'm a software engineer focused on backend and AI systems." />
                </div>
                {/* Right Panel(60%): Visual */}
                <div className="flex items-center justify-center bg-background-secondary px-2">
                    <HeroVisual />
                </div>
            </div>
        </section>
    );
};