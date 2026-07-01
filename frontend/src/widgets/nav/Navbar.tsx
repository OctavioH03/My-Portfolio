// Nav widget — top navigation bar with section links and scroll behavior
import { Link } from "react-router-dom";

const NAV_LINKS = [
    {label: "Home", href: "/"},
    {label: "About", href: "/about"},
    {label: "Projects", href: "/projects"},
    {label: "Contact", href: "/contact"},
]

export const Navbar = () => {
    return (
        <nav
            style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "1rem 2rem",
                background: "var(--surface-navy)",
                borderBottom: "1px solid var(--border-navy)",
            }}
        >
            <Link to="/" style={{ fontSize: "1.5rem", fontWeight: 700, color: "var(--accent)" }}>
                O∞H
            </Link>
            <div style={{ display: "flex", gap: "1.5rem" }}>
                {NAV_LINKS.map((link) => (
                    <Link key={link.href} to={link.href} style={{ color: "var(--text-secondary)" }}>
                        {link.label}
                    </Link>
                ))}
            </div>
        </nav>
    )
}
export default Navbar;