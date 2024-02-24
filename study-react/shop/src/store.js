import { configureStore, createSlice } from '@reduxjs/toolkit'

let user = createSlice({
  name: 'user',
  initialState : 'Kim',
  reducers : {
    changeName(state){
      return 'John' + state
    }
  }
})

export let { changeName } = user.actions

let cart = createSlice({
  name: 'useritem',
  initialState: [
    { id: 0, 
      name: 'White and Black', 
      count: 2 
    },
    { id: 2, 
      name: 'Grey Yordan', 
      count: 1 
    }
  ],
  reducers: {
    changeCount(state){
      return state + 1
    }
  }
});

export let { changeCount } = user.actions

export default configureStore({
  reducer: { 
    user: user.reducer,
    useritem: cart.reducer
  }
})