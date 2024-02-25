import { createSlice } from '@reduxjs/toolkit'

let user = createSlice({
  name: 'user',
  initialState : { name: 'Kim', age : 20},
  reducers : {
    changeName(state){
      return 'John' + state
    }
  }
})

export default user