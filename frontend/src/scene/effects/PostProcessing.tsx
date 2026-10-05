import { useThree } from "@react-three/fiber";
import { BloomEffect } from "./Bloom";
import { EffectComposer } from "@react-three/postprocessing";

import { OverrideMaterialManager } from 'postprocessing'

export function PostProcessing() {
    OverrideMaterialManager.workaroundEnabled = true

    const { scene, camera } = useThree();

    return (
        <EffectComposer
            scene={scene}
            camera={camera}
            enabled={true}
        >
            <BloomEffect />
        </EffectComposer>
    )
}