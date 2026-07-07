// Button — primary/secondary/ghost variants using accent token
import { type ButtonHTMLAttributes, forwardRef } from "react";
import { tv } from "tailwind-variants";

export type ButtonVariantStyle = "solid" | "ghost" | "outline";
export type ButtonVariantColor = "primary" | "secondary";
export type ButtonVariantSize = "xs" | "sm" | "md" | "lg" | "xl";

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    variantStyle?: ButtonVariantStyle;
    color?: ButtonVariantColor;
    size?: ButtonVariantSize;
}

const buttonVariants = tv({
    base: [
        "inline-flex items-center justify-center",
        "font-body font-semibold tracking-wide",
        "rounded transition-all duration-150",
        "focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent",
        "disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none",
        "whitespace-nowrap select-none",
    ],
    variants: {
        variantStyle: {
            solid: "", // filled in by compound variants below
            outline: "border bg-transparent",
            ghost: "bg-transparent",
        },
        color: {
            primary: "",
            secondary: "",
        },
        size: {
            xs: "text-xs px-2 py-1 gap-1.0",
            sm: "text-sm px-3 py-1.5 gap-1.5",
            md: "text-base px-4 py-2 gap-2",
            lg: "text-lg px-5 py-2.5 gap-2.5",
            xl: "text-xl px-6 py-3 gap-3",
        },
    },
    compoundVariants: [
        // solid buttons
        {
            variantStyle: "solid",
            color: "primary",
            class: "bg-accent text-background hover:bg-accent-dark focus-visible:outline-accent",
        },
        {
            variantStyle: "solid",
            color: "secondary",
            class: "bg-accent-secondary text-background hover:bg-accent-secondary-dark focus-visible:outline-accent-secondary"
        },
        // outline buttons
        {
            variantStyle: "outline",
            color: "primary",
            class: "border-accent text-accent hover:bg-accent/10 focus-visible:outline-accent",
        },
        {
            variantStyle: "outline",
            color: "secondary",
            class: "border-accent-secondary text-accent-secondary hover:bg-accent-secondary/10 focus-visible:outline-accent-secondary",
        },
        // ghost buttons
        {
            variantStyle: "ghost",
            color: "primary",
            class: "text-accent hover:bg-accent/10 focus-visible:outline-accent",
        },
        {
            variantStyle: "ghost",
            color: "secondary",
            class: "text-accent-secondary hover:bg-accent-secondary/10 focus-visible:outline-accent-secondary",
        },
    ],
    defaultVariants: {
        variantStyle: "solid",
        color: "primary",
        size: "md",
    },
});

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
    ({ variantStyle, color, size, className, children, ...htmlProps}, ref) => {
        return (
            <button
                ref={ref}
                className={buttonVariants({ variantStyle, color, size, class:className })}
                {...htmlProps}
            >
                {children}
            </button>
        );
    }
);

Button.displayName = "Button";