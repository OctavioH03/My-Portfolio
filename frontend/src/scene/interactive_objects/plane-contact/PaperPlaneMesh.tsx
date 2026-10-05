import { MeshTransmissionMaterial, useGLTF } from "@react-three/drei"
import { Vector3 } from "three"
import { useControls } from "leva"
import { useRef } from "react"
import { useFrame } from "@react-three/fiber"

export function PaperPlaneMesh({ position, rotation, scale }: { position: Vector3, rotation: Vector3, scale: number }) {
    const mesh = useRef();
    const { nodes } = useGLTF("/models/paper_plane.glb")

    useFrame(() => {
        mesh.current.rotation.y += 0.01
    })

    // Leva control for material properties
    // e.g. transmission: materialProps.transmission or <MeshTransmissionMaterial {...materialProps} />
    const materialProps = useControls({
        transmission: { value: 1, min: 0, max: 1, step: 0.01 },
        thickness: { value: 0.1, min: 0, max: 1, step: 0.01 },
        roughness: { value: 0, min: 0, max: 1, step: 0.01 },
        ior: { value: 1.4, min: 0, max: 2, step: 0.01 },
        chromaticAberration: { value: 0.2, min: 0, max: 1, step: 0.01 },
        distortion: { value: 0.15, min: 0, max: 1, step: 0.01 },
        distortionScale: { value: 0.2, min: 0, max: 1, step: 0.01 },
        temporalDistortion: { value: 0.05, min: 0, max: 1, step: 0.01 },
        backside: { value: false, label: "Backside" },
    })

    return (
        <group
            position={position}
            rotation={[rotation.x, rotation.y, rotation.z]}
            scale={scale}
        >
            <mesh ref={mesh} geometry={nodes.Paper_Plane.geometry}>
                <MeshTransmissionMaterial
                    transmission={materialProps.transmission}
                    thickness={materialProps.thickness}
                    roughness={materialProps.roughness}
                    ior={materialProps.ior}
                    chromaticAberration={materialProps.chromaticAberration}
                    distortion={materialProps.distortion}
                    distortionScale={materialProps.distortionScale}
                    temporalDistortion={materialProps.temporalDistortion}
                    backside={materialProps.backside}
                    emissive="white"
                    emissiveIntensity={0.05}
                />
            </mesh>
        </group>
    )
}

useGLTF.preload("/models/paper_plane.glb")
