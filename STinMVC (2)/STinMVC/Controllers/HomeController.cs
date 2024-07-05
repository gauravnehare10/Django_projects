using STinMVC.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace STinMVC.Controllers
{
    public class HomeController : Controller
    {
        // GET: Home
        public ActionResult Index()
        {
            Employee obj = new Employee();     
            return View(obj.GetAllEmployees());
            
        }

        // GET: Home/Details/5
        public ActionResult Details(int id)
        {
            Employee empObj = new Employee();
            return View(empObj.GetAllEmployees().Find(obj => obj.ItemID == id));

        }

        // GET: Home/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Home/Create
        [HttpPost]
        public ActionResult Create(Employee obj)
        {
            try
            {
                Employee emp = new Employee();
                emp.AddEmployee(obj);
                ModelState.Clear();
                ViewBag.Message = " Item Added Successfully";
                return View();
            }
            catch
            {
                return View();
            }
        }

        // GET: Home/Edit/5
        public ActionResult Edit(int id)
        {
            Employee emp = new Employee();
            return View(emp.GetAllEmployees().Find(obj => obj.ItemID == id));
        }

        // POST: Home/Edit/5
        [HttpPost]
        public ActionResult Edit(int id , Employee obj)
        {
            try
            {
                Employee emp = new Employee();
                emp.UpdateDetails(obj);
                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Home/Delete/5
        public ActionResult Delete(int id)
        {
           Employee emp = new Employee();
            var singleUser = emp.GetAllEmployees().Find(obj => obj.ItemID == id);
            return View(singleUser);

        }

        // POST: Home/Delete/5
        [HttpPost]
        public ActionResult Delete(int id, FormCollection collection)
        {
            try
            {
                Employee obj = new Employee();
                obj.DeleteStudent(id);
                ViewBag.AlertMsg = "Item Deleted Successfully";
                return RedirectToAction("Index");


            }
            catch
            {
                return View();
            }
        }
    }
}
