def min_points_to_cover_segments(segments):
    segments.sort(key=lambda x: x[1])
    points = []
    last_point = None

    for l, r in segments:
        if last_point is None or last_point < l:
            last_point = r
            points.append(last_point)
    return len(points), points


def main():
    with open('data_prog_contest_problem_1.txt') as f:
        lines = f.readlines()
    segments = [tuple(map(int, line.split())) for line in lines[1:]]
    result, points = min_points_to_cover_segments(segments)
    print(result)

if __name__ == '__main__':
    main()