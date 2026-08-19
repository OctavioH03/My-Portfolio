import { useRef } from "react";
import { Environment, useHelper } from "@react-three/drei";
import * as THREE from 'three';

export function RoomLighting({ directionalLightPosition, pointLightPosition, targetPosition }: { directionalLightPosition: THREE.Vector3, pointLightPosition: THREE.Vector3, targetPosition: THREE.Vector3 }) {
    const ENVIRONMENT_FILE = '/hdri/industrial_sunset_puresky_1k.hdr';
    const target = new THREE.Object3D();
    target.position.set(targetPosition.x, targetPosition.y, targetPosition.z);

    const light = useRef<THREE.DirectionalLight>(null!);
    const pointLight = useRef<THREE.PointLight>(null!);

    // DEBUGGING: helpers to see lights in scene
    // useHelper(light, THREE.DirectionalLightHelper, 1);
    // useHelper(pointLight, THREE.PointLightHelper, 1);

    return (
        <>
            <Environment
                files={ENVIRONMENT_FILE}
                backgroundIntensity={0.075} // no background light --> enclosed space
                environmentIntensity={0.1}
                background={true}
                backgroundRotation={[0, -Math.PI / 3.35, 0]}
            />

            {/* Sunlight */}
            <directionalLight
                ref={light}
                castShadow
                position={directionalLightPosition}
                target={target}
                intensity={2}
                color={0xFFF8DE} // more cold moonlight: 0xB8CFE8, more warm moonlight: FFF8DE
                shadow-mapSize={[2048, 2048]}
                shadow-bias={-0.0001}
                shadow-normalBias={0.001}
            />
            {/* Sublte Warm lighting for with in the room */}
            {/* <pointLight
                ref={pointLight}
                scale={0.1}
                position={pointLightPosition}
                intensity={6}
                color="#FFF8DE"
            /> */}
            <group position={[1.6, -3.05, 0]} >
                {/* The actual light — RectAreaLight matches a strip profile best */}
                <rectAreaLight
                    color="white"
                    intensity={3}
                    width={0.5}
                    height={2}
                    rotation={[-Math.PI / 2, 0, 0]}
                />
            </group>
        </>
    )
}