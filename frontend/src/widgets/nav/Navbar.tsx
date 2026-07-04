// Nav widget — top navigation bar with section links and scroll behavior

const NAV_LINKS = [
    {label: "Home", href: "#home"},
    {label: "About", href: "#about"},
    {label: "Projects", href: "#projects"},
    {label: "Contact", href: "#contact"},
]

export const Navbar = () => {
    return (
        <nav className= "fixed top-0 left-0 right-0 z-50 bg-background-secondary border-b border-border-primary py-2">
            <div className= "flex items-center justify-between">
                <div className= "items-center">
                    {/* TODO: Add logo here as a link to the home page */}
                    <a href="#home" className= "font-display font-bold text-2xl text-text-secondary hover:text-text-primary hover:text-3xl px-4 py-2">
                        O∞H
                    </a>
                </div>          
                <div className= "flex items-center">
                    {/* TODO: Make navigation links clickable, scrolling to corresponding section on page */}
                    {NAV_LINKS.map((link) => (
                        <a 
                        key={link.href} 
                        href={link.href} 
                        className= "font-body font-semibold text-lg text-text-secondary border-transparent hover:text-text-primary px-4 py-2 border-b-2 hover:border-border-primary hover:border-border-secondary">
                            {link.label}
                        </a>
                    ))}
                </div>
            </div>
        </nav>
    )
}