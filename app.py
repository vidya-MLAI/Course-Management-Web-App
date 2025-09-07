import streamlit as st
import db

# Reset DB once if table is old
# db.reset_db()  # <-- Uncomment once if your table lacks fees/mode

db.init_db()

st.title("📚 Course Management App")

menu = ["Add Course", "View Courses", "Update Course", "Delete Course"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- Add Course ----------------
if choice == "Add Course":
    st.subheader("Add New Course")
    title = st.text_input("Course Title")
    description = st.text_area("Description")
    instructor = st.text_input("Instructor")
    duration = st.text_input("Duration")
    fees = st.text_input("Fees")
    mode = st.selectbox("Mode", ["Online", "Offline"])

    if st.button("Add Course"):
        if title.strip():
            db.add_course(title, description, instructor, duration, fees, mode)
            st.success(f"✅ Course '{title}' added successfully!")
        else:
            st.warning("⚠️ Title cannot be empty.")

# ---------------- View Courses ----------------
elif choice == "View Courses":
    st.subheader("All Courses")
    courses = db.get_courses()
    if courses:
        for course in courses:
            st.markdown(f"### {course[1]}")  # Bigger title
            st.markdown(f"**Description:** {course[2]}")
            st.markdown(f"**Instructor:** {course[3]}  |  **Duration:** {course[4]}  |  **Fees:** {course[5]}  |  **Mode:** {course[6]}")
            st.markdown("---")
    else:
        st.info("No courses available.")

# ---------------- Update Course ----------------
elif choice == "Update Course":
    st.subheader("Update Course")
    courses = db.get_courses()
    if courses:
        course_dict = {course[1]: course for course in courses}
        selected_title = st.selectbox("Select a Course to Update", list(course_dict.keys()))
        selected_course = course_dict[selected_title]

        new_title = st.text_input("New Title", selected_course[1])
        new_description = st.text_area("New Description", selected_course[2])
        new_instructor = st.text_input("Instructor", selected_course[3])
        new_duration = st.text_input("Duration", selected_course[4])
        new_fees = st.text_input("Fees", selected_course[5])
        new_mode = st.selectbox("Mode", ["Online", "Offline"], index=["Online","Offline"].index(selected_course[6]))

        if st.button("Update"):
            db.update_course(selected_course[0], new_title, new_description, new_instructor, new_duration, new_fees, new_mode)
            st.success("✅ Course updated successfully!")
    else:
        st.info("No courses available to update.")

# ---------------- Delete Course ----------------
elif choice == "Delete Course":
    st.subheader("Delete Course")
    courses = db.get_courses()
    if courses:
        course_dict = {course[1]: course for course in courses}
        selected_title = st.selectbox("Select Course to Delete", list(course_dict.keys()))
        if st.button("Delete"):
            db.delete_course(course_dict[selected_title][0])
            st.success(f"❌ Course '{selected_title}' deleted successfully!")
    else:
        st.info("No courses to delete.")
