import { useRef } from "react";
import { Environment, useHelper } from "@react-three/drei";
import * as THREE from 'three';

export function RoomLighting({ position, targetPosition }: { position: THREE.Vector3, targetPosition: THREE.Vector3 }) {
    const ENVIRONMENT_FILE = '/hdri/industrial_sunset_puresky_1k.hdr';
    const target = new THREE.Object3D();
    target.position.set(targetPosition.x, targetPosition.y, targetPosition.z);

    const light = useRef<THREE.DirectionalLight>(null!);

    // DEBUGGING: helpers to see lights in scene
    // useHelper(moonlight, THREE.DirectionalLightHelper, 1);
      
    return (
        <>
            <Environment
                files={ENVIRONMENT_FILE}
                backgroundIntensity={0.075} // no background light --> enclosed space
                environmentIntensity={0.1}
                background={true}
                backgroundRotation={[0, -Math.PI / 3.35, 0]}
            />

            {/* Moonlight */}
            <directionalLight
                ref={light}
                castShadow
                position={position}
                target={target}
                intensity={6}
                color={0xFFF8DE} // more cold moonlight: 0xB8CFE8, more warm moonlight: FFF8DE
                shadow-mapSize={[2048,2048]}
                shadow-bias={-0.0001}
                shadow-normalBias={0.001}
            />
        </>
    )
}