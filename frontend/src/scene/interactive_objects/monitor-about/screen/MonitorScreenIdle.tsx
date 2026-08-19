import { PerspectiveCamera, RenderTexture } from '@react-three/drei'
import { useRef } from 'react';
import { MeshStandardMaterial, Vector3 } from 'three'
import { ScreenHeader } from './MonitorScreenHeader';
import { ScreenBorder } from './ScreenBorder';

export default function MonitorScreenIdle({ position }: { position: Vector3 }) {

    const materialRef = useRef<MeshStandardMaterial>(null!)

    return (
        <mesh position={position}>
            <planeGeometry attach="geometry" args={[0.7, 0.3825]} />
            <meshStandardMaterial
                ref={materialRef}
                toneMapped={false}
                emissiveIntensity={1.2}
                transparent={true}
                opacity={0.2}
                depthWrite={false}
                roughness={1}
            >
                <RenderTexture attach="map" samples={4}>
                    <PerspectiveCamera
                        makeDefault
                        position={[0, 0, 5]}
                        manual={true}
                        aspect={16 / 9}
                        fov={75}
                    />
                    <color attach="background" args={['transparent']} />
                    <ambientLight
                        color="lightblue"
                        intensity={30}
                    />
                    <ScreenBorder />
                    <ScreenHeader position={[0, 0, 0]} />
                </RenderTexture>
            </meshStandardMaterial>
        </mesh>
    )
}