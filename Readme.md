# FastAPI JWT Authentication System

## **Project Description**
A scalable FastAPI project with JWT-based authentication integrated with MongoDB. It includes user CRUD operations with role-based access control (RBAC) and secure endpoints.

---

## **Features**

### Must-Have Features
1. **Login and Logout Endpoints**:
   - Users can log in to receive a JWT and log out by invalidating tokens.

2. **Secure Endpoints for User CRUD**:
   - Protected routes for creating, reading, updating, and deleting users.

3. **Readable Code**:
   - Code is modular and well-documented.

4. **No ODM Library**:
   - MongoDB interaction is implemented using the `motor` library.

5. **User Creation Script**:
   - Predefined database and collection setup included.

### Good-to-Have Features
1. **Logging**:
   - Integrated logging for debugging and tracking events.

2. **Predefined Models**:
   - Models defined using Pydantic for user and token validation.

3. **MongoDB Atlas**:
   - Fully compatible with an online MongoDB database.

4. **Scalable Code Structure**:
   - Modularized to support extensions and scaling.

### Added Bonus
1. **RBAC (Role-Based Access)**:
   - Role validation for different user types.

---

## **Setup Instructions**

### Prerequisites
- Python 3.9 or higher
- Virtual environment (recommended)
- MongoDB Atlas account

### Steps to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-jwt-auth.git
   cd fastapi-jwt-auth
   
###
I have also not connected mt mongodb atlas to this this is a sample project and the logging is working
