// Hero Left Panel: text and buttons
import { Button } from "../../shared/ui/Button";
import { RiSendPlaneFill } from "react-icons/ri";

type HeroContentProps = {
    title: string;
    description: string;
}

export const HeroContent = ({ title, description }: HeroContentProps) => {
    return (
        <div className="flex flex-col gap-2">
            <h1 className="font-display text-6xl font-bold text-text-primary">{title}</h1>
            <p className="font-body font-semibold text-lg text-text-muted max-w-2xl">{description}</p>
            <div className="flex flex-row justify-end gap-4 py-12">
                <Button variantStyle="solid" color="primary" size="md">
                    Contact
                    <RiSendPlaneFill size={20}/>
                </Button>
                <Button variantStyle="ghost" color="primary" size="md">Learn More</Button>
            </div>
        </div>
    )
}