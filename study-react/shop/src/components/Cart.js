import { Table } from 'react-bootstrap'
import { useSelector, useDispatch } from 'react-redux'
import { changeName, changeCount } from '../store.js'


function Cart(){

  let user = useSelector((state) => state.user);
  let cart = useSelector((state) => state.useritem);
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
            <td>{[i+1]}</td>
            <td>{cart[i].name}</td>
            <td>{cart[i].count}</td>
            <td>
              <button onClick={()=>{
                dispatch(changeCount())
              }}>+</button>
            </td>
          </tr>
            )
          }

        </tbody>
      </Table>
    </div>
  )
}
export default Cart