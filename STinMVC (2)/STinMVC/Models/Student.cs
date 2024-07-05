using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Data;
using System.Linq;
using System.Web;

namespace STinMVC.Models
{
    public class Student
    {
        public int TransID { get; set; }    
        public int ItemID { get; set; } 
        public string TransType { get; set; }
        public int TransQty { get; set; }



        public List<Student> GetAllEmployees()
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");
            // var con = connection();

            con.Open();
            List<Student> EmpList = new List<Student>();

            var query = "select * from Transactions";
            SqlCommand cmd = new SqlCommand(query, con);
            SqlDataAdapter da = new SqlDataAdapter(cmd);

            DataTable dt = new DataTable();
            da.Fill(dt);

            con.Close();

            foreach (DataRow dr in dt.Rows)
            {
                EmpList.Add(
                new Student
                {
                    TransID = Convert.ToInt32(dr["TransID"]),
                    ItemID = Convert.ToInt32(dr["ItemID"]),
                    TransType = Convert.ToString(dr["TransType"]),
                    TransQty = Convert.ToInt32(dr["TransQty"]),

                });
            }
            return EmpList;
        }


        public void AddEmployee(Student obj)
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");
            con.Open();
            string query = "insert into Transactions(ItemID,TransQty,TransType) values( '" + obj.ItemID + "','" + obj.TransQty + "','" + obj.TransType + "')";
            SqlCommand cmd = new SqlCommand(query, con);
            cmd.ExecuteNonQuery();

            con.Close();
            updateItem(obj.ItemID ,obj.TransQty);
        }

        public void updateItem(int id , int qty)
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");
            con.Open();
            string query = "update ItemMaster set BalQty = BalQty - @TransQty where ItemID = @ItemID";

            SqlCommand cmd = new SqlCommand(query, con);
            cmd.Parameters.AddWithValue("@TransQty", qty);
            cmd.Parameters.AddWithValue("@ItemID",id);
            cmd.ExecuteNonQuery();

            con.Close();

        }

        public void DeleteStudent(int id)
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");


            con.Open();

            string query = "Delete from Transactions where TransID= " + id;
       
            SqlCommand cmd = new SqlCommand(query, con);
          

            cmd.ExecuteNonQuery();

            con.Close();
           
        }


        public void UpdateDetails(Student obj)
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");
           con.Open();
            
           string query = "Update Transactions set TransQty=" + "'" + obj.TransQty + "'" + "where TransID = " + obj.TransID;
             SqlCommand cmd = new SqlCommand(query, con);
           
            cmd.ExecuteNonQuery();
        
            con.Close();

          
        }


     
    }

}
