use std::convert::TryInto;
use std::env;

fn main() {
    let list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    let args: Vec<String> = env::args().collect();
    let number_to_be_searched = args[1].parse::<i32>().unwrap();

    println!(
        "Searching for {} in {:?}",
        number_to_be_searched, list_of_numbers
    );

    let position_in_list = binary_search(&list_of_numbers, number_to_be_searched);

    if position_in_list >= 0 {
        println!(
            "The position of {} in the list is {}.",
            number_to_be_searched, position_in_list
        );
    } else {
        println!("Not found.");
    }
}

fn binary_search(list_of_numbers: &[i32], x: i32) -> i32 {
    let mut low: i32 = 0;
    let mut high: i32 = list_of_numbers.len().try_into().unwrap();

    let mut mid: i32;
    let mut guess: i32;

    if high != 0 {
        high = high - 1;
    }

    while low <= high {
        mid = (low + high) / 2 as i32;
        guess = list_of_numbers[mid as usize];

        if guess == x {
            return mid;
        } else if guess > x {
            high = mid - 1 as i32;
        } else {
            low = mid + 1 as i32;
        }
    }
    return -1;
}
