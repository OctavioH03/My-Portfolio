import { useMemo } from "react"
import { MeshStandardMaterial } from "three"


export function ScreenBorder({
    width = 13.25,
    height = 7.35, 
    thickness = 0.05,
    color = "white"
}) {
    const halfWidth = width / 2
    const halfHeight = height / 2
    
    const material = useMemo(() => new MeshStandardMaterial({
        color,
        emissive: color,
        emissiveIntensity: 400,
        toneMapped: false,
    }), [color])

    return (
        <group>
            {/* Top border */}
            <mesh position={[0, halfHeight, 0]} material={material} >
                <planeGeometry args={[width, thickness]} />
            </mesh>
            {/* Bottom border */}
            <mesh position={[0, -halfHeight, 0]} material={material} >
                <planeGeometry args={[width, thickness]} />
            </mesh>
            {/* Right border */}
            <mesh position={[halfWidth, 0, 0]} material={material} >
                <planeGeometry args={[thickness, height]} />
            </mesh>
            {/* Left border */}
            <mesh position={[-halfWidth, 0, 0]} material={material} >
                <planeGeometry args={[thickness, height]} />
            </mesh>
        </group>
    )
}