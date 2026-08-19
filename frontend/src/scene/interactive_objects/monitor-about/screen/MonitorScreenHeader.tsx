// screen/ScreenHeader.tsx
import { Text } from '@react-three/drei'
import { useMemo } from 'react'
import { MeshStandardMaterial } from 'three'

export function ScreenHeader({ position }: { position: [number, number, number] }) {

    const contentMaterial: Map<string, MeshStandardMaterial> = useMemo(() => new Map([
        ["monogram", new MeshStandardMaterial({
            color: "#7DF9FF",
            emissive: "#7DF9FF",
            emissiveIntensity: 120,
        })],
        ["infinity", new MeshStandardMaterial({
            color: "white",
            emissive: "white",
            emissiveIntensity: 100,
        })],
        ["horizontalLine", new MeshStandardMaterial({
            color: "white",
            emissive: "white",
            emissiveIntensity: 400,
        })],
        ["name", new MeshStandardMaterial({
            color: "#FFFFFF",
            emissive: "#FFFFFF",
            emissiveIntensity: 180,
        })],
        ["role", new MeshStandardMaterial({
            color: "#4FC3F7",
            emissive: "#4FC3F7",
            emissiveIntensity: 150,
        })],
    ]), [])
    return (
        <group position={position}>
            {/* O∞H monogram — larger, accent cyan */}
            <Text
                fontSize={2}
                anchorX="center"
                anchorY="middle"
                letterSpacing={1}
                position={[0, 1.6, 0]}
                outlineWidth={0.06}
                outlineBlur={0.01}
                material={contentMaterial.get("monogram")}
            >
                O
                <Text
                    fontSize={2.5}
                    position={[0, -0.1, 0]}
                    material={contentMaterial.get("infinity")}
                >
                    &infin;
                </Text>
                H
            </Text>
            {/* Horizontal line below monogram */}
            <mesh position={[0, 0.3, 0]} material={contentMaterial.get("horizontalLine")}>
                <planeGeometry args={[8, 0.01]} />
            </mesh>
            {/* Full name — smaller, below monogram */}
            <Text
                position={[0, -0.45, 0]}
                fontSize={0.5}
                anchorX="center"
                anchorY="middle"
                letterSpacing={0.12}
                outlineColor="black"
                outlineWidth={0.005}
                material={contentMaterial.get("name")}
            >
                OCTAVIO HERNANDEZ
            </Text>

            {/* Role subtitle */}
            <Text
                position={[0, -1.2, 0]}
                fontSize={0.4}
                anchorX="center"
                anchorY="middle"
                letterSpacing={0.06}
                outlineColor="black"
                outlineWidth={0.005}
                outlineOpacity={0.6}
                material={contentMaterial.get("role")}
            >
                Software Engineer
            </Text>
        </group>
    )
}