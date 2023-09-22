pub mod test;
use test::test_run_all;


fn dijkstra(matrix: Vec<Vec<i32>>, start: usize, end: usize) {
    let count_vertices = matrix.len();
    let mut queue: Vec<usize> = vec![start; 1];
    let mut minimum_routes: Vec<i32> = vec![-1; count_vertices];
    minimum_routes[start] = matrix[start][start];
    while queue.len() != 0 {
        let current_position = queue.pop().unwrap();
        for i in 0..count_vertices {
            if matrix[current_position][i] == 0 { continue; }
            let minmal_path_len = if minimum_routes[i] == -1 {i32::MAX} else {minimum_routes[i]};
            if matrix[current_position][i] + minimum_routes[current_position] < minmal_path_len {
                minimum_routes[i] = matrix[current_position][i] + minimum_routes[current_position];
                queue.push(i);
            }
        }
    }
    let mut path_len = minimum_routes[end];
    let mut current_position = end;
    let mut minimum_path = [end].to_vec();
    if path_len == -1 {
        println!("Путь не существует!");
        return;
    }
    while path_len != 0 {
        for i in 0..count_vertices {
            if i == current_position || matrix[i][current_position] == 0 {continue;}
            if path_len - matrix[i][current_position] == minimum_routes[i] {
                minimum_path.push(i);
                path_len -= matrix[i][current_position];
                current_position = i;
                break;
            }
        }
    }
    minimum_path.reverse();
    println!("Мин маршрут до каждой вершины: {:?}", minimum_routes);
    println!("Маршрут имеет длину: {}", minimum_routes[end]);
    println!("Маршрут построен: {:?}", minimum_path);
}


fn main() {
    if false { test_run_all(); return ; }
    let _m = vec![
        vec![0, 190, 137, 416, 429],
        vec![0, 0, 219, 0, 43],
        vec![0, 0, 0, 0, 0],
        vec![67, 0, 298, 0, 0],
        vec![0, 0, 0, 289, 0],
    ];

    let _start = 3;
    let _end = 4; 
    dijkstra(_m.clone(), _start, _end);
}

