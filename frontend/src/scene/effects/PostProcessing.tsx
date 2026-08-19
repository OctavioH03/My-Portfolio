import { useThree } from "@react-three/fiber";
import { BloomEffect } from "./Bloom";
import { EffectComposer } from "@react-three/postprocessing";
import * as THREE from "three";

import { OverrideMaterialManager } from 'postprocessing'

// interface PostProcessingProps {
//     scene: THREE.Scene;
//     camera: THREE.Camera;
// }

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