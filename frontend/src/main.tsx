import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./app/App";
import "./app/styles/fonts.css";
import "./app/styles/index.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter basename="/"> {/* add loading state for fallback */} 
      <App />
    </BrowserRouter>
  </StrictMode>,
);
