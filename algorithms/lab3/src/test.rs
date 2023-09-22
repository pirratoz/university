fn dijkstra(matrix: Vec<Vec<i32>>, start: usize, end: usize) -> (Vec<i32>, i32, Vec<usize>) {
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
        return ([].to_vec(), 0, [].to_vec());
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
    // println!("Мин маршрут до каждой вершины: {:?}", minimum_routes);
    // println!("Маршрут имеет длину: {}", minimum_routes[end]);
    // println!("Маршрут построен: {:?}", minimum_path);
    return (minimum_routes.clone(), minimum_routes[end].clone(), minimum_path.clone());
}


pub fn test_case_1(){
    let _m = vec![
        vec![0, 2, 0, 0, 0, 0, 0, 15, 0],
        vec![2, 0, 1, 5, 0, 0, 0, 0, 0],
        vec![0, 1, 0, 3, 0, 2, 1, 0, 0],
        vec![0, 5, 3, 0, 6, 4, 0, 0, 0],
        vec![0, 0, 0, 6, 0, 7, 0, 0, 2],
        vec![0, 0, 2, 4, 7, 0, 1, 3, 0],
        vec![0, 0, 1, 0, 0, 1, 0, 0, 0],
        vec![15, 0, 0, 0, 0, 3, 0, 0, 0, 12],
        vec![0, 0, 0, 0, 2, 0, 0, 12, 0],
    ];
    if dijkstra(_m.clone(), 0, 8) == (vec![0, 2, 3, 6, 12, 5, 4, 8, 14], 14, vec![0, 1, 2, 3, 4, 8]) {
        println!("micro test (1) - 1: pass")
    }
    if dijkstra(_m.clone(), 0, 4) == (vec![0, 2, 3, 6, 12, 5, 4, 8, 14], 12, vec![0, 1, 2, 3, 4]) {
        println!("micro test (1) - 2: pass")
    }
    if dijkstra(_m.clone(), 0, 7) == (vec![0, 2, 3, 6, 12, 5, 4, 8, 14], 8, vec![0, 1, 2, 5, 7]) {
        println!("micro test (1) - 3: pass")
    }
}


pub fn test_case_2(){
    let _m = vec![
        vec![0, 190, 137, 416, 429],
        vec![0, 0, 219, 0, 43],
        vec![0, 0, 0, 0, 0],
        vec![67, 0, 298, 0, 0],
        vec![0, 0, 0, 289, 0],
    ];
    if dijkstra(_m.clone(), 3, 4) == (vec![67, 257, 204, 0, 300], 300, vec![3, 0, 1, 4]) {
        println!("micro test (2) - 1: pass")
    }
    if dijkstra(_m.clone(), 3, 2) == (vec![67, 257, 204, 0, 300], 204, vec![3, 0, 2]) {
        println!("micro test (2) - 2: pass")
    }
    if dijkstra(_m.clone(), 2, 0) == (vec![0; 0], 0, vec![0; 0]) {
        println!("micro test (2) - 3: pass")
    }
}


pub fn test_run_all() {
    test_case_1();
    test_case_2();
}
