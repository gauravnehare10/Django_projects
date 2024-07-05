using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Web;
using System.Web.UI.WebControls.WebParts;


namespace STinMVC.Models
{
    public class Employee
    {
        public int ItemID { get; set; }
    public  string ItemDescr { get; set; }
      public  int BalQty { get; set; }

        public SqlConnection connection()
        {
            string _connectionString =   ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString;
            SqlConnection con = new SqlConnection(_connectionString);
            return con;
        }

        public List<Employee> GetAllEmployees()
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");
           // var con = connection();
           
            con.Open();
            List<Employee> EmpList = new List<Employee>();
            
            var query = "select * from ItemMaster";
            SqlCommand cmd = new SqlCommand(query, con);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
         
            DataTable dt = new DataTable();
            da.Fill(dt);
           
            con.Close();
   
            foreach (DataRow dr in dt.Rows)
            {
                EmpList.Add(
                new Employee
                {
                    ItemID = Convert.ToInt32(dr["ItemID"]),
                    ItemDescr = Convert.ToString(dr["ItemDescr"]),
                    BalQty = Convert.ToInt32(dr["BalQty"]),

                });
            }
            return EmpList;
        }


        public void AddEmployee(Employee obj)
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");        
            con.Open();         
           string query = "insert into ItemMaster(ItemDescr,BalQty) values( '" + obj.ItemDescr + "','" + obj.BalQty + "')";
            SqlCommand cmd = new SqlCommand(query, con);      
            cmd.ExecuteNonQuery();
          
            con.Close();
        }

        public void DeleteStudent(int id)
        {
            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");

           
            con.Open();
            
            string query = "Delete from ItemMaster where ItemID=" + id;
            SqlCommand cmd = new SqlCommand(query, con);
           
            cmd.ExecuteNonQuery();
         
            con.Close();
        }

       
        public void UpdateDetails(Employee obj)
        {

            SqlConnection con = new SqlConnection("data source=DESKTOP-E8J08GK\\SQLEXPRESS;database=employee;integrated security=yes");

            con.Open();
         
        string query = "Update ItemMaster set ItemDescr=" + "'" +obj.ItemDescr + "'" + " , BalQty= " + "'" + obj.BalQty + "'" + " where  ItemID = " + obj.ItemID;

            SqlCommand cmd = new SqlCommand(query, con);
          
            cmd.ExecuteNonQuery();
        
            con.Close();
        }

       
    }
}