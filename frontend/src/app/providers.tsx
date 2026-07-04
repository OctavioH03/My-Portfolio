// Providers — wraps the app with global context providers (e.g. TanStack Query, theme)
import type { ReactNode } from "react";

interface ProvidersProps {
    children: ReactNode;
}

export const Providers = ({ children }: ProvidersProps) => {
    return (
        <>
            {children}
        </>
    )
}