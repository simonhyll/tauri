#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use libc::c_char;
use libc::printf;
use once_cell::sync::OnceCell;
use std::ffi::CStr;
use std::ffi::CString;
use std::sync::Mutex;
use tauri::{Builder, Wry};

// static APP: OnceCell<Box<Builder<Wry>>> = OnceCell::new();

#[no_mangle]
pub extern "C" fn init() {
  // APP.set(tauri::Builder::default().any_thread());
}

#[no_mangle]
pub extern "C" fn run(arg: *const c_char) {
  let c_str = unsafe { CStr::from_ptr(arg) };
  let str_slice: &str = c_str.to_str().unwrap();
  let str_buf: String = str_slice.to_owned(); // if you want to keep it
  println!("Rust received string: {:?}", str_buf);
  tauri::Builder::default().any_thread();
}

#[no_mangle]
pub extern "C" fn get_name() -> *mut c_char {
  let s = CString::new("Hello!").unwrap();
  s.into_raw()
}

#[no_mangle]
pub extern "C" fn free_get_name(c: *mut c_char) {
  // convert the pointer back to `CString`
  // it will be automatically dropped immediately
  unsafe {
    let _ = CString::from_raw(c);
  }
}
