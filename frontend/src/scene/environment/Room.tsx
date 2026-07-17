import { useGLTF } from "@react-three/drei"; 
import { useEffect } from "react";
import * as THREE from 'three';

export function Room({ position }: { position: THREE.Vector3 }) {
    const { scene } = useGLTF('/models/office_room.glb')

    useEffect(() => {
        scene.traverse((child) => {
            if (child instanceof THREE.Mesh) {
                child.castShadow = true
                child.receiveShadow = true
                if (child.name.startsWith('WindowPanes_')) {
                    child.material.transmission = 0.95
                    child.castShadow = false
                }
            }
        })
    }, [scene])

    return (
        <primitive 
            object={scene} 
            rotation={[0, -Math.PI / 2, 0]}
            position={position}
            scale={1}
        />
    );
}

useGLTF.preload("/models/office_room.glb");