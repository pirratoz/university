mod edges;
use std::collections::VecDeque;
use edges::{
    Edges,
    get_edges
};


fn dfs(graph: & Edges, viseted: &mut Vec<usize>, start: usize, end: usize, count_path: &mut u32){
    if start == end {
        *count_path += 1;
        if true {
            viseted.push(end);
            println!("{:?}", viseted);
            viseted.pop();
        }
    }

    viseted.push(start);
    let index = viseted.len() - 1;

    if graph.contains_key(&start) {
        for i in graph[&start].clone() {
            if ! viseted.contains(&i.v) {
                dfs(graph, viseted, i.v, end, count_path);
            }
        }
    }

    viseted.remove(index);
}

fn bfs(graph: & Edges, start: usize, n: usize) -> Vec<i32> {
    let mut distance = vec![100_000; n];
    let mut queue: VecDeque<usize> = VecDeque::new();

    distance[start] = 0;
    queue.push_back(start);

    while !queue.is_empty() {
        let v = queue.pop_front().unwrap();
        
        if !graph.contains_key(&v) { continue; }

        for i in graph[&v].clone() {
            if distance[i.v] > distance[v] + 1 {
                distance[i.v] = distance[v] + 1;
                queue.push_back(i.v);
            }
        }
    }
    return distance;
}


fn main() {
    let _m = vec![
        vec![0, 1, 1, 1, 1],
        vec![0, 0, 1, 0, 1],
        vec![0, 0, 0, 0, 0],
        vec![1, 0, 1, 0, 0],
        vec![0, 0, 0, 1, 0],
    ];
    let mut visited: Vec<usize> = Vec::new();
    let mut count_path = 0;

    let graph: Edges = get_edges(_m.clone());
    let start = 1;
    let end = 2;

    dfs(&graph, &mut visited, start, end, &mut count_path);

    println!("Найдено: {} маршрутов\n", count_path);

    let distance = bfs(&graph, start, _m.len());
    println!("Длины маршрутов: {:?}", distance);
}
