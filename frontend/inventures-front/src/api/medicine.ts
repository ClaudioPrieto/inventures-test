import axios, { AxiosResponse } from "axios";

const BASE_URL = 'https://private-anon-c6a779afff-inventurestest.apiary-mock.com/products';

export const getMedicineList = async () => {
  let currenciesResponse: AxiosResponse

  try {
    currenciesResponse = await axios.get(BASE_URL)
    return currenciesResponse.data.payload
  } catch (error) {
    return null
  }
}
