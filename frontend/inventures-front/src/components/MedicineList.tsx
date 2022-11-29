import { getMedicineList } from "../api/medicine";
import { useEffect, useState } from "react";
import MedicineItem from "./MedicineItem";

const MedicineList = () => {
  const [medicineList, setMedicineList] = useState<any[]>([]);

  useEffect(() => {
    getMedicineList().then((response) => {
      setMedicineList(response);
    });
  }, []);
    
  return (
      <div>
        <div className="bg-gray-100">
          <p className="font-medium pb-1 pt-[7px] px-4 text-[19px]">
            Te queda
          </p>
        </div>
        <div className='body'>
        

          <div>
            {medicineList.map((medicine, index) => (
              <div key={ index }>
                <MedicineItem {...medicine}/>
                <hr />
              </div>
            ))}
          </div>
        </div>
      </div>
  );
}

export default MedicineList;
