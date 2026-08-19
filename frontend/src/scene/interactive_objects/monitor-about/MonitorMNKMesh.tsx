import { MeshTransmissionMaterial, useGLTF, useFBO } from "@react-three/drei";
import { Camera, Scene, Vector3, WebGLRenderer } from "three";
import { useFrame } from "@react-three/fiber";
import MonitorScreenIdle from "./screen/MonitorScreenIdle";


export function MonitorMNKMesh({ position, rotation }: { position: Vector3, rotation: Vector3 }) {
    const { nodes } = useGLTF("/models/monitor_mnk.glb")

    const buffer = useFBO()
    useFrame((state: { gl: WebGLRenderer, scene: Scene, camera: Camera }) => {
        state.gl.setRenderTarget(buffer)
        state.gl.render(state.scene, state.camera)
        state.gl.setRenderTarget(null)
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
                        transmission={0.9}
                        thickness={0.05}
                        emissive="blue"
                        emissiveIntensity={0.05}
                        buffer={buffer.texture}
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