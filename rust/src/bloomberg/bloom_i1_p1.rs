//! # Description
//!
//! Given a list of "Events," return a list of occupied time-blocks
//!
//! - events are represented as tuples: (start, end, event_name)
//!     - start is simply a number, you don't need to be concerned about AM/PM
//!     - end is simply a number, you don't need to be concerned about AM/PM
//!     - assume all events hold valid times where 0 <= start <= end and both start and time are valid integers (no decimals)
//!     - event_name is simply a string with the name of the event
//! - return a list of "time-blocks" such that each contiguous block of scheduled time is represented
//!     - each time block should have a start time and an end time
//!     - output is not necessarily the same length as input list
//!     - event_names should not be featured in output
//!     - output does not need to be sorted
//!
//! # Example
//!
//! input_001 = [
//!     (100, 300, "event"),
//!     (115, 245, "event"),
//!     (200, 400, "event"),
//!     (600, 700, "event"),
//!     (500, 600, "event"),
//! ]
//! expected_001 = [
//!     [100, 400],
//!     [500, 700],
//! ]
//!
//! if expected_001 = time_blocks(input_001):
//!     print("TEST_PASSED")
//! else:
//!     print("TEST_FAILED")

pub struct BloombergI1P1;

impl BloombergI1P1 {
    pub fn time_blocks(mut intervals: Vec<(u32, u32)>) -> Vec<(u32, u32)> {
        if intervals.is_empty() {
            return vec![];
        }

        intervals.sort();

        let (mut first, mut second) = intervals[0];

        let mut res: Vec<(u32, u32)> = vec![];

        for (start, end) in intervals.iter() {
            if start > &second {
                res.push((first.clone(), second.clone()));
                first = start.clone();
                second = end.clone()
            } else if end > &second {
                second = end.clone();
            } else if start < &first {
                first = start.clone();
            }
        }
        res.push((first.clone(), second.clone()));

        res
    }
}

#[cfg(test)]
mod tests {
    use super::BloombergI1P1;

    #[test]
    fn test_001() {
        let input = vec![(100, 300), (115, 245), (200, 400), (600, 700), (500, 600)];
        let expected = vec![(100, 400), (500, 700)];

        let actual = BloombergI1P1::time_blocks(input);

        assert_eq!(actual, expected);
    }

    #[test]
    fn test_002() {
        assert_eq!(
            vec![] as Vec<(u32, u32)>,
            BloombergI1P1::time_blocks(vec![])
        );
    }
}
