fn print_matrix(message: &str, matrix: &Vec<Vec<i32>>, n: usize) { println!("{}", message); for i in 0..n { println!("{:?}", matrix[i]) } }


fn get_path(matrix_p: &Vec<Vec<i32>>, mut start: usize, end: usize) -> Vec<i32> {
    let mut path = [].to_vec();
    loop {
        if start as i32 == -1 {break;}
        path.push(start as i32);
        start = matrix_p[start][end] as usize;
    }
    path.push(end as i32);
    path
}

fn main() {
    let m = vec![
        vec![0, 0, 5, 0, 0],
        vec![7, 0, 0, 0, 10],
        vec![0, 7, 0, 0, 0],
        vec![0, 0, 3, 0, 4],
        vec![0, 0, 1, 0, 0]
    ];
    let n = m.len();

    let start = 3;
    let end = 0;

    let mut w = m.clone();
    let mut wt = m.clone();
    let mut p = vec![vec![-1; n]; n];

    // заполняем пути "бесконечностью"
    (0..n).for_each(|i: usize| (0..n).for_each(|j: usize|
        if i != j && wt[i][j] == 0 { wt[i][j] = i32::MAX }
    ));

    (0..n).for_each(|k: usize| (0..n).for_each(|i: usize| (0..n).for_each(|j: usize | {
        w[i][j] = (w[i][j] > 0 || (w[i][k] > 0 && w[k][j] > 0)) as i32;
        if wt[i][k] != i32::MAX && wt[k][j] != i32::MAX && (wt[i][j] > wt[i][k] + wt[k][j]) {
            wt[i][j] = wt[i][k] + wt[k][j];
            p[i][j] = k as i32;
        }
    })));
    
    // убираем "бесконечность" и ставим -1
    (0..n).for_each(|i: usize| (0..n).for_each(|j: usize|
        if wt[i][j] == i32::MAX { wt[i][j] = -1 }
    ));

    print_matrix("Main matrix:", &m, n);
    print_matrix("Warshell matrix:", &w, n);
    print_matrix("Weights matrix:", &wt, n);
    print_matrix("Previous matrix:", &p, n);

    println!("");

    let mut e = vec![0; n];
    for i in 0..n {
        for j in 0..n {
            if i != j { e[i] += 1; }
        }
    }
    let r = e.iter().min().unwrap();
    let d = e.iter().max().unwrap();
    let mut mids = vec![0; 0];
    (0..n).for_each(|i| if &e[i] == r {mids.push(i)});
    println!("R={}\nD={}\nmid's={:?}\ne={:?}", r, d, mids, e);

    println!("");

    let path = get_path(&p, start, end);
    if path.get(0) == path.get(1) {
        println!("Начальная точка совпадает с конечной");
    } else if path.len() == 2 {
        println!("Маршрут не существует");
    } else {
        println!("Маршрут: {:?}\nДлина маршрута: {}", path, wt[start][end]);
    }
}