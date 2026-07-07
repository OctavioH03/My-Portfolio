// Nav widget — top navigation bar with section links and scroll behavior
import { GiInfinity } from "react-icons/gi";

const NAV_LINKS = [
    {label: "Hero", href: "#hero"},
    {label: "About", href: "#about"},
    {label: "Projects", href: "#projects"},
    {label: "Contact", href: "#contact"},
]

export const Navbar = () => {
    return (
        <nav className= "fixed top-0 left-0 right-0 z-50 bg-background-secondary border-b-2 border-border-primary py-2">
            <div className= "flex flex-row items-center justify-between">
                <div className= "px-4">
                    {/* TODO: Add logo here as a link to the home page */}
                    <a href="#hero" className= "flex flex-row items-center font-display font-bold text-2xl text-text-secondary tracking-wide hover:text-text-primary hover:text-3xl">
                        O
                        <GiInfinity size={20} className="text-text-primary hover:text-text-secondary hover:scale-115 transition-all duration-300"/>
                        H
                    </a>
                </div>          
                <div className= "flex items-center">
                    {/* TODO: Make navigation links clickable, scrolling to corresponding section on page */}
                    {NAV_LINKS.map((link) => (
                        <a 
                        key={link.href} 
                        href={link.href} 
                        className= "font-body font-semibold text-lg text-text-primary tracking-wide border-transparent hover:text-text-secondary px-4 py-2 border-b-2 hover:border-border-primary hover:border-border-secondary">
                            {link.label}
                        </a>
                    ))}
                </div>
            </div>
        </nav>
    )
}