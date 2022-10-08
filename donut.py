from math import pi, sin, cos

W, H = 80, 25

SPEED_A, SPEED_B, SPEED_I, SPEED_J = (
    0.05, 0.05, 0.05, 0.05
)

CHARS = ".,-~:;=!*#$@"
PI2 = 2 * pi


def calculate_screen(screen: list) -> str:
    return (
        "\33[2J"    # Clear screen
        "\33[H"     # Move cursor to top left
        "\33[?25l"  # Hide cursor
    ) + "".join(
        "\n" if i % W == 0 else c for i, c in enumerate(screen)
    )

a = b = 0

while True:
    grid, _grid = [" "] * H * W, [0] * 4 * H * W

    j = 0
    while j < PI2:
        j += SPEED_I
        i = 0

        while i < PI2:
            i += SPEED_J

            sa, sb, sc, sd, ca, cb, cc, cd = (
                *map(sin, (a, b, i, j)), *map(cos, (a, b, i, j))
            )
            e, f = 1/(sc*(cd+2)*sa+sd*ca+5), sc*(cd+2)*ca-sd*sa

            index = int(
                (x := int(W/2+30*e*(cc*(cd+2)*cb-f*sb)))
                + W * (y := int(H/2+15*e*(cc*(cd+2)*sb+f*cb)))
            )
            if 0 < y < H and 0 < x < W and _grid[index] < e:
                z = int(8*((sd*sa-sc*cd*ca)*cb-sc*cd*sa-sd*ca-cc*cd*sb))

                _grid[index] = e  # type: ignore
                grid[index] = CHARS[max(z, 0)]

    print(calculate_screen(grid))

    a += SPEED_A
    b += SPEED_B
