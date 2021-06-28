pub struct LeetCode013;
impl LeetCode013 {
    pub fn roman_to_int_better(s: String) -> i32 {
        fn rtoi(ch: char) -> i32 {
            match ch {
                'I' => 1,
                'V' => 5,
                'X' => 10,
                'L' => 50,
                'C' => 100,
                'D' => 500,
                'M' => 1000,
                _ => 0,
            }
        }

        let mut ret: i32 = 0;

        for (idx, ch) in s.chars().enumerate() {
            ret += match idx {
                0 => rtoi(ch),
                _ => {
                    let prev = rtoi(s.chars().nth(idx - 1).unwrap());
                    let mut curr = rtoi(ch);

                    if prev < curr {
                        curr -= prev + prev;
                    }

                    curr
                }
            }
        }

        ret
    }
    // MDCCCLXXXIV
    // M        1000        1000
    // D        500          500
    // CCC      100 * 3      300
    // L        50            50
    // XXX      10 * 3        30
    // IV       4              4
    // -------------------------
    //                      1884
    pub fn roman_to_int(s: String) -> i32 {
        fn rtoi(ch: char) -> u32 {
            match ch {
                'M' => 1000_u32,
                'D' => 500_u32,
                'C' => 100_u32,
                'L' => 50_u32,
                'X' => 10_u32,
                'V' => 5_u32,
                'I' => 1_u32,
                _ => 0,
            }
        }

        fn is_esc_key(ch: char) -> bool {
            match ch {
                'I' | 'X' | 'C' => true,
                _ => false,
            }
        }

        fn is_valid_exception(prev: char, current: char) -> bool {
            match (prev, current) {
                ('I', 'V') | ('I', 'X') | ('X', 'L') | ('X', 'C') | ('C', 'D') | ('C', 'M') => true,
                _ => false,
            }
        }

        let mut s_chars = s[..].chars();
        let mut total_sum: u32 = 0;

        let mut last_is_escaped: Option<char> = None;

        while let Some(current_char) = s_chars.next() {
            if let Some(reducer) = last_is_escaped {
                if is_valid_exception(reducer, current_char) {
                    total_sum += rtoi(current_char) - rtoi(reducer);
                    last_is_escaped = None;
                } else {
                    total_sum += rtoi(reducer);
                    last_is_escaped = Some(current_char);
                }
            } else if is_esc_key(current_char) {
                last_is_escaped = Some(current_char);
            } else {
                total_sum += rtoi(current_char)
            }
        }

        if let Some(reducer) = last_is_escaped {
            total_sum += rtoi(reducer)
        }

        total_sum as i32
    }
}

#[cfg(test)]
mod tests {
    use super::LeetCode013;

    #[test]
    fn test_001() {
        assert_eq!(3, LeetCode013::roman_to_int(String::from("III")));
    }

    #[test]
    fn test_002() {
        assert_eq!(4, LeetCode013::roman_to_int(String::from("IV")));
    }

    #[test]
    fn test_003() {
        assert_eq!(9, LeetCode013::roman_to_int(String::from("IX")));
    }

    #[test]
    fn test_004() {
        assert_eq!(58, LeetCode013::roman_to_int(String::from("LVIII")));
    }

    #[test]
    fn test_005() {
        assert_eq!(1994, LeetCode013::roman_to_int(String::from("MCMXCIV")))
    }

    #[test]
    fn test_006() {
        assert_eq!(1884, LeetCode013::roman_to_int(String::from("MDCCCLXXXIV")))
    }

    #[test]
    fn test_007() {
        assert_eq!(1570, LeetCode013::roman_to_int(String::from("MDLXX")))
    }
}
