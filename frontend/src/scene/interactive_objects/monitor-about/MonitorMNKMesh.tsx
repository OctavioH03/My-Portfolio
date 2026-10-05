import { MeshTransmissionMaterial, useGLTF, useFBO } from "@react-three/drei";
import { Camera, Scene, Vector3, WebGLRenderer } from "three";
import { useFrame } from "@react-three/fiber";
import MonitorScreenIdle from "./screen/MonitorScreenIdle";
import { useControls } from "leva";


export function MonitorMNKMesh({ position, rotation }: { position: Vector3, rotation: Vector3 }) {
    const { nodes } = useGLTF("/models/monitor_mnk.glb")

    const buffer = useFBO()
    useFrame((state: { gl: WebGLRenderer, scene: Scene, camera: Camera }) => {
        state.gl.setRenderTarget(buffer)
        state.gl.render(state.scene, state.camera)
        state.gl.setRenderTarget(null)
    })

    // Use this for testing the material properties, just assign each mesh material property to the specific materialProps
    // e.g. thickness: materialProps.thickness or <MeshTransmissionMaterial {...materialProps} />
    const materialProps = useControls({
        thickness: { value: 0.35, min: 0, max: 1, step: 0.01 },
        chromaticAberration: { value: 0.2, min: 0, max: 1, step: 0.01 },
        transmission: { value: 0.9, min: 0, max: 1, step: 0.01 },
        emissive: { value: "blue", options: ["blue", "red", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "black", "white"] },
        emissiveIntensity: { value: 0.05, min: 0, max: 1, step: 0.01 },
        roughness: { value: 0.5, min: 0, max: 1, step: 0.01 },
        ior: { value: 1.5, min: 1, max: 2, step: 0.01 },
        distortion: { value: 0.2, min: 0, max: 1, step: 0.01 },
        distortionScale: { value: 1, min: 0, max: 10, step: 0.1 },
        temporalDistortion: { value: 0.2, min: 0, max: 1, step: 0.01 },
        backside: { value: false, label: "Backside" },
    })

    return (
        <group position={position} rotation={[rotation.x, rotation.y, rotation.z]}>
            {/* Monitor Frame */}
            <mesh
                geometry={nodes.monitor.children[0].geometry}
            >
                <MeshTransmissionMaterial
                    thickness={0.35}
                    chromaticAberration={0.2}
                    buffer={buffer.texture}
                />
            </mesh>
            <group>
                {/* Glass Screen Panel */}
                <mesh
                    geometry={nodes.monitor.children[1].geometry}
                >
                    <MeshTransmissionMaterial
                        // transmission={0.9}
                        // thickness={0.05}
                        // chromaticAberration={0.2}
                        // emissive="blue"
                        // emissiveIntensity={0.05}
                        // buffer={buffer.texture}
                        {...materialProps}
                    />

                </mesh>
                <MonitorScreenIdle
                    position={new Vector3(0, 0.2625, 0)}
                />
            </group>


            {/* Mouse */}
            <mesh
                geometry={nodes.mouse.geometry}
            >
                <MeshTransmissionMaterial
                    thickness={0.1}
                    buffer={buffer.texture}
                />
            </mesh>
            {/* Keyboard */}
            <mesh
                geometry={nodes.keyboard.geometry}
            >
                <MeshTransmissionMaterial
                    thickness={0.1}
                    buffer={buffer.texture}
                />
            </mesh>
        </group>
    )
}

useGLTF.preload("/models/monitor_mnk.glb");