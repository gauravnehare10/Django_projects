using STinMVC.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace STinMVC.Controllers
{
    public class StudentController : Controller
    {
        // GET: Student
        public ActionResult Index()
        {
            Student obj = new Student();
            return View(obj.GetAllEmployees());
        }

        // GET: Student/Details/5
        public ActionResult Details(int id)
        {
            Student empObj = new Student();
            return View(empObj.GetAllEmployees().Find(obj => obj.TransID == id));

        }

        // GET: Student/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Student/Create
        [HttpPost]
        public ActionResult Create(Student obj)
        {
            try
            {

                Student std  = new Student();
                std.AddEmployee(obj);
                ModelState.Clear();
                ViewBag.Message = " Item Added Successfully";
                return View();
            }
            catch
            {
                return View();
            }
        }

        // GET: Student/Edit/5
        public ActionResult Edit(int id)
        {
            Student  emp = new Student();
            return View(emp.GetAllEmployees().Find(obj => obj.TransID == id));
        }

        // POST: Student/Edit/5
        [HttpPost]
        public ActionResult Edit(int id, Student obj)
        {
            try
            {
                Student  emp = new Student();
                emp.UpdateDetails(obj);
                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Student/Delete/5
        public ActionResult Delete(int id)
        {
            Student emp = new Student();
            var singleUser = emp.GetAllEmployees().Find(obj => obj.TransID == id);
            return View(singleUser);
        }

        // POST: Student/Delete/5
        [HttpPost]
        public ActionResult Delete(  int id, FormCollection  formCollection)
        {
            try
            {
                Student emp = new Student();
                emp.DeleteStudent(id);
                ViewBag.Alertmsg = "Transaction deleted";
                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }
    }
}
