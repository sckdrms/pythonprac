import { Table } from 'react-bootstrap'
import { useSelector, useDispatch } from 'react-redux'
import { changeCount, addItem } from '../store.js'
import { changeName } from '../store/userSlice.js'


function Cart(){

  let user = useSelector((state) => state.user.name);
  let cart = useSelector((state) => state.cart);
  let dispatch = useDispatch()

  return(
    <div>

      {user}의 장바구니

      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>변경하기</th>
          </tr>
        </thead>
        <tbody>
          {
            cart.map((a, i)=>
            <tr key={i}>
            <td>{cart[i].id}</td>
            <td>{cart[i].name}</td>
            <td>{cart[i].count}</td>
            <td>
              <button onClick={() => {
                dispatch(changeCount({ id: cart[i].id, amount: 1 }));
                }}>+</button>
            </td>
          </tr>
            )
          }
        <button onClick={console.log({cart})}>다 보기</button>
        </tbody>

      </Table>
    </div>
  )
}
export default Cart