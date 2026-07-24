import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { getAllCourses } from '../../api/courseApi';

// Async Thunk
export const fetchAllCourses = createAsyncThunk(
  'courses/fetchAll',
  async () => {
    return await getAllCourses();
  }
);

const courseSlice = createSlice({
  name: 'courses',

  initialState: {
    courses: [],
    loading: false,
    error: null
  },

  reducers: {},

  extraReducers: (builder) => {
  builder

    // Pending
    .addCase(fetchAllCourses.pending, (state) => {
      state.loading = true;
      state.error = null;
    })

    // Fulfilled
    .addCase(fetchAllCourses.fulfilled, (state, action) => {
      state.loading = false;
      state.courses = action.payload;
    })

    // Rejected
    .addCase(fetchAllCourses.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
}
});

// Selectors
export const selectCourses = (state) => state.courses.courses;

export const selectCoursesLoading = (state) => state.courses.loading;

export const selectCoursesError = (state) => state.courses.error;

export default courseSlice.reducer;