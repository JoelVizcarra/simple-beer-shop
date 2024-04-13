'use client'
import { useState, useEffect } from 'react'
import axios from 'axios'

interface OrderItem {
  name: string
  quantity: number
}

interface OrderRound {
  created: string
  items: OrderItem[]
}

interface Order {
  created: string
  paid: boolean
  subtotal: number
  taxes: number
  discounts: number
  items: OrderItem[]
  rounds: OrderRound[]
}

// move to env config
const API_URL = 'http://localhost:8000'

const OrderPage = ({ params }: { params: { id: string } }) => {
  const { id } = params
  const [order, setOrder] = useState<Order | null>(null)

  useEffect(() => {
    const fetchOrder = async () => {
      try {
        const response = await axios.get(`${API_URL}/orders/${id}`)
        setOrder(response.data)
      } catch (error) {
        console.error('Error fetching order:', error)
      }
    }

    if (id) {
      fetchOrder()
    }
  }, [id])

  return (
    <div className="bg-gray-900 text-white min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-8">Order</h1>
      {order ? (
        <div>
          <p className="mb-4">Created: {order.created}</p>
          <p className="mb-4">Paid: {order.paid ? 'Yes' : 'No'}</p>
          <div className="mb-4">
            <h2 className="text-xl font-bold mb-2">Items:</h2>
            <ul>
              {order.items.map((item, index) => (
                <li key={index} className="mb-2">
                  {item.quantity} x {item.name}
                </li>
              ))}
            </ul>
          </div>
          <div className="mb-4">
            <h2 className="text-xl font-bold mb-2">Rounds:</h2>
            <ul>
              {order.rounds.map((round, index) => (
                <li key={index} className="mb-4">
                  <p className="mb-2">Created: {round.created}</p>
                  <ul>
                    {round.items.map((item, index) => (
                      <li key={index} className="mb-2">
                        {item.quantity} x {item.name}
                      </li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>
          </div>
          <p className="mb-4">Subtotal: ${order.subtotal}</p>
          <p className="mb-4">Taxes: ${order.taxes}</p>
          <p className="mb-4">Discounts: ${order.discounts}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  )
}

export default OrderPage
