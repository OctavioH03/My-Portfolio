// App — root component: mounts providers, router, and the home page
import Navbar from "../widgets/nav/Navbar";

export const App = () => {
    return (
        <div style={{ minHeight: "100vh", background: "var(--background)" }}>
            <Navbar />
        </div>
    )
}
export default App;