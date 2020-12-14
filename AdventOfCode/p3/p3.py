import re

def read_file():
    with open('input.txt', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        return lines

def find_patches(file_lines):
    patches = []
    p = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')
    for line in file_lines:
        m = p.match(line)
        patches.append({'id': int(m.group(1)),
                        'x': int(m.group(2)),
                        'y': int(m.group(3)),
                        'w': int(m.group(4)),
                        'h': int(m.group(5))})
    return patches

def build_matrix():
    matrix = [[0] * 1500 for _ in range(1500)]
    return matrix

def patches_to_matrix(patches, matrix):
    for patch in patches:
        for row_idx in range(patch['y'], patch['y'] + patch['h']):
            for col_idx in range(patch['x'], patch['x'] + patch['w']):
                matrix[row_idx][col_idx] += 1

def find_overlapping_area(matrix):
    overlapping_area = 0
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] > 1:
                overlapping_area += 1
    return overlapping_area

def find_nonoverlapping_patch(patches, matrix):
    for patch in patches:
        patch_overlaps = False
        for row_idx in range(patch['y'], patch['y'] + patch['h']):
            for col_idx in range(patch['x'], patch['x'] + patch['w']):
                if matrix[row_idx][col_idx] > 1:
                    patch_overlaps = True
                    break
            if patch_overlaps:
                break
        if not patch_overlaps:
            return patch

    return None


file_lines = read_file()
patches = find_patches(file_lines)
matrix = build_matrix()
patches_to_matrix(patches, matrix)
overlapping_area = find_overlapping_area(matrix)
print(overlapping_area)
nonoverlapping_patch = find_nonoverlapping_patch(patches, matrix)
print(nonoverlapping_patch)
