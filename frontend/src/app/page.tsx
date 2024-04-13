import Link from 'next/link'

const Home = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-4 text-center mt-4">
        Simple Beer Shop
      </h1>
      <div className="flex justify-center items-center h-screen bg-gray-900 text-white">
        <div className="bg-gray-800 rounded-lg shadow-lg p-8 max-w-md">
          <h2 className="text-2xl font-bold mb-4">Última Orden</h2>
          <ul>
            <li className="border-b py-2">
              <Link
                className="text-blue-400 hover:text-blue-600"
                href="/orders/2030ba80-eff4-416d-a1bf-9dcef0e40cc3"
              >
                Orden #2030ba80-eff4-416d-a1bf-9dcef0e40cc3
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default Home
