import math

def calculate_velocity(initial_velocity, acceleration, time):
    """Calculates final velocity: v = u + at"""
    return initial_velocity + (acceleration * time)

def calculate_projectile_range(velocity, angle_degrees, gravity=9.81):
    """Calculates horizontal range of a projectile in physics."""
    angle_rad = math.radians(angle_degrees)
    range_val = (velocity ** 2 * math.sin(2 * angle_rad)) / gravity
    return round(range_val, 2)

print("=== Python Physics & Mechanics Utility ===")

# Test Kinematics Calculation
u, a, t = 0.0, 9.81, 5.0
final_v = calculate_velocity(u, a, t)
print(f"\nKinematics Test:")
print(f"Initial Velocity: {u} m/s, Acceleration: {a} m/s², Time: {t}s")
print(f"Calculated Final Velocity: {final_v} m/s")

# Test Projectile Motion Calculation
v_init, angle = 20.0, 45.0
proj_range = calculate_projectile_range(v_init, angle)
print(f"\nProjectile Motion Test:")
print(f"Launch Velocity: {v_init} m/s, Angle: {angle}°")
print(f"Calculated Horizontal Range: {proj_range} meters")

print("\nPhysics utility script executed successfully on mobile environment!")
