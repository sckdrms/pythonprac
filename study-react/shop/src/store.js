import { configureStore, createSlice } from '@reduxjs/toolkit'
import user from './store/userSlice.js'


let cart = createSlice({
  name: 'cart',
  initialState: [
    { id: 0, name: 'White and Black', count: 0 },
    { id: 2, name: 'Grey Yordan', count: 0 }
  ],
  reducers: {
    changeCount(state, action) {
      // action.payload에서 id와 amount를 추출합니다.
      const { id, amount } = action.payload;
      // id에 해당하는 아이템을 찾습니다.
      const item = state.find(item => item.id === id);
      if (item) {
        // 해당 아이템의 count를 amount만큼 변경합니다.
        item.count += amount;
      }
    }  
    ,
  addItem(state,action){
    state.push(action.payload)
  }
  }
});

export let { changeCount, addItem } = cart.actions



export default configureStore({
  reducer: { 
    user: user.reducer,
    cart: cart.reducer
  }
})