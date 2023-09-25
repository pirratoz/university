mod edges;
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
    let start = 0;
    let end = 2;

    dfs(&graph, &mut visited, start, end, &mut count_path);

    println!("Найдено: {} маршрутов\n", count_path);
}
